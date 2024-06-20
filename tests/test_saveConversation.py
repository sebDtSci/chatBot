import pytest
import pandas as pd
import streamlit as st
from unittest.mock import patch, MagicMock
from src.saveConversation import delete_conversation

@pytest.fixture
def mock_load_conversations():
    with patch('src.saveConversation.load_conversations') as mock:
        yield mock

@pytest.fixture
def mock_to_csv():
    with patch('pandas.DataFrame.to_csv') as mock:
        yield mock

@pytest.fixture
def mock_sidebar_success():
    with patch('streamlit.sidebar.success') as mock:
        yield mock

@pytest.fixture
def mock_sidebar_error():
    with patch('streamlit.sidebar.error') as mock:
        yield mock

@pytest.mark.parametrize("title,df_data,expected_df_data", [
    ("Conversation1", pd.DataFrame({"Titre": ["Conversation1", "Conversation2"]}), pd.DataFrame({"Titre": ["Conversation2"]})),
    ("Conversation2", pd.DataFrame({"Titre": ["Conversation1", "Conversation2"]}), pd.DataFrame({"Titre": ["Conversation1"]})),
    ("NonExistent", pd.DataFrame({"Titre": ["Conversation1", "Conversation2"]}), pd.DataFrame({"Titre": ["Conversation1", "Conversation2"]})),
], ids=["delete_first", "delete_second", "delete_nonexistent"])
def test_delete_conversation_happy_path(title, df_data, expected_df_data, mock_load_conversations, mock_to_csv, mock_sidebar_success):

    # Arrange
    mock_load_conversations.return_value = df_data

    # Act
    delete_conversation(title)

    # Assert
    pd.testing.assert_frame_equal(mock_load_conversations.return_value, df_data)
    mock_to_csv.assert_called_once_with("data/conversations.csv", index=False, sep=";")
    mock_sidebar_success.assert_called_once_with("Conversation supprimée avec succès !")

@pytest.mark.parametrize("title,df_data", [
    ("", pd.DataFrame({"Titre": ["Conversation1", "Conversation2"]})),
    (None, pd.DataFrame({"Titre": ["Conversation1", "Conversation2"]})),
], ids=["empty_title", "none_title"])
def test_delete_conversation_edge_cases(title, df_data, mock_load_conversations, mock_to_csv, mock_sidebar_success):

    # Arrange
    mock_load_conversations.return_value = df_data

    # Act
    delete_conversation(title)

    # Assert
    pd.testing.assert_frame_equal(mock_load_conversations.return_value, df_data)
    mock_to_csv.assert_called_once_with("data/conversations.csv", index=False, sep=";")
    mock_sidebar_success.assert_called_once_with("Conversation supprimée avec succès !")

@pytest.mark.parametrize("exception,expected_message", [
    (FileNotFoundError("File not found"), "Erreur lors de la suppression de la conversation: File not found"),
    (PermissionError("Permission denied"), "Erreur lors de la suppression de la conversation: Permission denied"),
], ids=["file_not_found", "permission_denied"])
def test_delete_conversation_error_cases(exception, expected_message, mock_load_conversations, mock_sidebar_error):

    # Arrange
    mock_load_conversations.side_effect = exception

    # Act
    delete_conversation("AnyTitle")

    # Assert
    mock_sidebar_error.assert_called_once_with(expected_message)
