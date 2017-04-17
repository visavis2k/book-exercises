# -*- coding: cp949 -*-
# �� ���� �����ϱ�
def break_words(stuff):
    """�� �Լ��� ���ڿ��� �ܾ�� �ɰ� �ݴϴ�."""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """�ܾ �����մϴ�."""
    return sorted(words)
    
def print_first_word(words):
    """ù �ܾ ������ ����մϴ�."""
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """������ �ܾ ������ ����մϴ�."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """�� ������ ��°�� �޾� �ܾ �����ؼ� ��ȯ�մϴ�."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """������ ó���� ������ �ܾ ����մϴ�."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """�ܾ �����ϰ� ó���� ������ �ܾ ����մϴ�."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
