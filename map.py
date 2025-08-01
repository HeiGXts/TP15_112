# 0 = grassTile1
# 1 = grassTile2
# 2 = treeTile1
# 3 = treeTile2
# 4 = treeTile3
# 5 = bushTile
# 6 = rockTile
# 7 = houseTile1
# tuple(u, d, l, r, e) = pathTile

#Inspiration from:
#https://kevins-moms-house.itch.io/fantasy

images = ['images/grassTile1.png', 'images/grassTile2.png', 'images/treeTile1.png', 'images/treeTile2.png', 'images/treeTile3.png',
          'images/bushTile.png', 'images/rockTile.png'
          ]

u = (-1, 0)
d = (1, 0)
l = (0, -1)
r = (0, 1)
e = (0, 0)

start = [(0, 1), (0, 7), (0, 3), (0, 17), (11, 2), (0, 13)]

enemyWave = [
    [[5, 0, 0, 0], [8, 0, 0, 0], [15, 0, 0, 0], [25, 0, 0, 0], [15, 0, 1, 0]], 
    [[8, 0, 0, 0], [10, 0, 0, 0], [10, 2, 0, 0], [20, 3, 1, 0], [15, 5, 1, 0], [15, 5, 3, 0]],
    [[12, 0, 0, 0], [15, 1, 0, 0], [15, 3, 1, 0], [25, 5, 2, 0], [15, 8, 3, 0], [20, 5, 3, 1]],
    [[15, 0, 0, 0], [15, 3, 1, 0], [20, 3, 1, 0], [25, 5, 3, 0], [18, 8, 3, 1], [10, 10, 3, 2]],
    [[15, 1, 0, 0], [18, 3, 1, 0], [20, 5, 1, 0], [25, 5, 2, 0], [18, 8, 3, 1], [20, 5, 1, 1], [20, 10, 5, 3]]
]

enemySpawnRate = [
    [60, 60, 55, 45, 60], 
    [60, 50, 50, 50, 50, 40], 
    [50, 45, 45, 50, 45, 40],
    [40, 40, 40, 35, 40, 40],
    [40, 35, 35, 35, 30, 30, 35]
]

reward = [(100, 10), (150, 15), (200, 20), (250, 25), (300, 30)]

money = [100, 120, 150, 180, 220]

worldMap = [
    [2, d, 0, 0, 2, 3, 3, 3, 3, 3, 4, 5, 0, 0, 0, 0, 0, 1, 1, 1],
    [2, d, 0, 0, 0, 2, 3, 3, 3, 2, 4, 0, r, r, r, r, r, d, 0, 0],
    [2, r, r, d, 0, 0, 5, 2, 3, 2, 0, r, u, 0, 1, 1, 0, r, r, e],
    [3, 2, 0, d, 0, 0, 0, 0, 2, 0, 0, u, 0, 1, 1, 1, 1, 0, 0, 0],
    [3, 4, 0, d, 0, 0, 0, 0, 0, 0, 0, u, l, l, l, 0, 1, 1, 0, 0],
    [4, 5, 0, r, r, r, d, 0, 0, 5, 6, 0, 0, 0, u, l, l, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, d, 0, 0, 0, 0, 0, 4, 2, 0, 0, u, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, r, r, r, r, d, 0, 6, 5, 0, r, u, 0, 0, 0],
    [4, 5, 0, 1, 1, 1, 0, 0, 0, 0, d, 0, 0, 0, 0, u, 0, 0, 0, 0],
    [2, 3, 2, 0, 0, 5, 0, 6, 0, 0, r, r, r, r, r, u, 0, 0, 0, 4],
    [3, 3, 3, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3],
    [3, 3, 3, 3, 3, 2, 3, 0, 5, 0, 0, 0, 6, 0, 0, 1, 1, 1, 3, 2],
]

level1 = [
    [3, 3, 3, 3, 2, 2, 4, d, 0, 0, 0, 0, 0, 4, 2, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 0, 0, d, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3],
    [3, 3, 3, 2, 2, 1, 0, d, 0, 0, 1, 1, 1, 0, 0, 4, 3, 3, 3, 3],
    [3, 3, 3, 4, 1, 1, 0, d, 0, 0, 0, 1, 1, 1, 1, 0, 2, 3, 3, 3],
    [2, 2, 2, 1, 0, 0, 0, d, 0, 0, 0, 0, 1, 1, 0, 0, 4, 2, 3, 3],
    [4, 0, 0, 0, d, l, l, l, 0, 2, 5, 0, 0, 4, 0, 0, 0, 0, 2, 4],
    [0, 5, 0, 0, d, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 4, 0, 0, d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, e],
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 5, 0, 0],
    [3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
]

level2 = [
    [0, 0, 0, d, 0, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, d, 0, 0, 0, 0, 0, 2, 4, 0, 0, 0, 1, 1, 4, 0, 0, 0],
    [0, 0, 0, d, 0, 0, 0, r, r, r, r, d, 0, 0, 1, 2, 2, 2, 0, 0],
    [0, 0, 0, d, 0, 0, 0, u, 0, 0, 0, d, 0, 0, 2, 3, 3, 3, 0, 0],
    [0, 1, 0, d, 1, 1, 1, u, 0, 0, 0, d, 0, 0, 2, 3, 3, 3, 0, 0],
    [0, 1, 1, d, 1, 0, 0, u, 0, 0, 0, d, 0, 4, 2, 3, 2, 4, 0, 0],
    [0, 1, 1, d, 0, 0, 0, u, 0, 0, 0, d, 0, 0, 3, 3, 1, 0, 0, 0],
    [0, 0, 1, d, 0, 5, 0, u, 0, 4, 0, d, 0, 0, 4, 1, 5, 0, 0, 0],
    [0, 0, 0, d, 0, 0, 0, u, 6, 2, 0, d, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, r, r, r, r, u, 0, 0, 0, d, 0, 0, 0, 0, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, d, 0, 5, 0, 0, 0, 6, 0, 0],
    [0, 6, 1, 1, 1, 1, 0, 0, 0, 0, 0, e, 0, 0, 0, 0, 0, 0, 0, 0],
]

level3 = [
    [3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d, 0, 0],
    [3, 3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, d, 0, 0],
    [2, 4, 0, 0, 0, 1, 1, 0, d, l, l, 0, 0, 0, 1, 5, 0, d, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, d, 0, u, 0, 0, 0, 0, 0, 0, d, 0, 0],
    [0, 0, 0, 0, d, l, l, l, l, 0, u, l, l, l, l, l, l, l, 0, 0],
    [0, 0, 0, 0, d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, d, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, r, r, r, d, 0, 0, 0, 1, 3, 3, 3, 2, 0, 0, 0, 0],
    [0, 0, 1, 5, 0, 0, 0, d, 0, 0, 1, 5, 3, 3, 3, 2, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, d, l, l, 0, 0, 1, 1, 3, 3, 3, 3, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, d, 0, 0, 0, 0, 0, 0, 6, 2, 3, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, e, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
]

level4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, r, r, r, r, r, r, r, r, r, r, r, r, r, r, d, 0, 1, 0],
    [0, 0, u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d, 1, 1, 0],
    [0, 0, u, 0, d, l, l, l, l, l, l, l, l, l, l, l, l, 1, 1, 0],
    [0, 0, u, 0, d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, u, 0, r, r, r, r, r, r, r, r, r, r, r, d, 0, 1, 1, 0],
    [1, 0, u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, d, 0, 0, 1, 0],
    [1, 0, u, 0, 0, 0, 0, 0, 5, 1, 1, 4, 0, 0, 0, d, 0, 0, 0, 0],
    [0, 0, u, 0, 0, 0, 0, 1, 1, 4, 2, 2, 1, 0, 0, d, 0, 0, 0, 0],
    [0, 0, u, 0, 0, 0, 0, 1, 3, 3, 3, 2, 0, 0, 0, d, 0, 0, 0, 0],
    [0, 0, u, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 4, 0, e, 0, 0, 0, 0],
]

level5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, d, l, l, l, l, l, 0, d, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, d, l, 0, 0, 0, 0, u, l, l, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, d, 0, 6, 1, 6, 0, 6, 0, 0, 5, 0, 1, 1, 0, 0],
    [0, 0, 6, 0, 0, d, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, d, 1, 1, 6, r, r, r, r, r, d, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, d, 1, 1, 1, u, d, l, l, 0, d, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, d, 1, 6, 1, u, l, 0, u, 0, d, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, d, 1, 1, 1, 1, 0, 0, u, 0, d, 0, 0, 0, 6, 0],
    [0, 0, 6, 1, 0, r, d, 0, 0, 6, 0, r, u, 0, d, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, r, r, r, r, r, u, 0, 0, d, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e, 0, 0, 0, 0, 0],
]

