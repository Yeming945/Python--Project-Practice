import random
""" 猜字游戏 """

# 创建单词序列
WORDS = ('python', 'jumble', 'easy', 'difficult',
         'phone', 'position', 'pose', 'game')

# 开始游戏
print(
    """
        欢迎参加猜单词游戏
    把字母组合成一个正确的单词
    """)

iscontinue = 'y'
while iscontinue == 'y' or iscontinue == 'Y':
    word = random.choice(WORDS)
    correct = word
    jumble = ''
    while word:
        # 根据word长度产生word的随机位置
        position = random.randrange(len(word))
        # 将postion位置的字母组合到乱序后单词
        jumble += word[position]
        # 通过切片将postion位置的字母从原单词中删除
        word = word[:position] + word[(position + 1):]
    print('乱序后单词: ', jumble)

    guess = input('\n请你猜: ')
    while guess != correct and guess != '':
        print('不正确!')
        guess = input('请继续猜: ')

        if guess == correct:
            print('你猜对了!')
    iscontinue = input('\n是否继续(Y/N): ')
