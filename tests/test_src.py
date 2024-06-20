from generateS import Generate
from memory import ChatbotMemory

def test_memory():
    mem = ChatbotMemory()
    mem.update_memory('test', 'test')
    assert mem.get_memory() == ["'user': test, 'bot': test"]

def test_generate():
    mod = Generate(model='test')
    assert mod.model == 'test'