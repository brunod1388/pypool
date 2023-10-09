from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()

# test = 3
# t = 1
# for elem in ft_tqdm(range(test)):
#     sleep(t)
# print()
# for elem in tqdm(range(0,10,2)):
#     print(elem)
#     sleep(t)
# print()
# for element in range(0, 10,2):
#     print(element)
