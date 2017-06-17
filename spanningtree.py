import pygame
from collections import deque

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
FONT = pygame.font.SysFont('Arial', 25)
#SCREEN.blit(FONT.render('b1', True, (255,0,0)), (75,75))
#pygame.display.update()
pygame.event.set_allowed(None)
done =False

#graph = {'b1':['l1','l2'],'l1':['b2'],'l2':['b3','b4'],'b2':['l3'],'b3':['l2','l3','l4'],'b4':['l2','l4'],'l3':['b2','b3','b5'],'l4':['b3','b4','b5'],
         #'b5':['l3','l4']}
g1={'b1':(50, 50),'b2':(500, 50),'b3':(275, 275),'b4':(50, 500),
    'b5':(500, 500),'l1':(275, 50),'l2':(50, 275),'l3':(500, 275),'l4':(275, 500)} #(k, v) k = name, v = (x,y)
graph={i:[] for i in g1}

for i in sorted(g1):
	if i.startswith('l'):
		continue
	for j in input("enter the nodes connected to %s:\n" %i).split():
		graph[i].append(j)
		graph[j].append(i)


def bfs(graph, start,end):
    d=deque()
    # push the first path into the queue
    d.append([start])
    while d:
        # get the first path from the queue
        path =d.popleft()
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and pushit into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            #print(new_path)
            new_path.append(adjacent)
            d.append(new_path)

SCREEN.fill((0, 0, 0))

for i in graph:
    if i.startswith('l'):
        continue
    for j in graph[i]:
        pygame.draw.line(SCREEN, (255, 255, 255), (g1[i][0] + 25, g1[i][1] + 25), (g1[j][0] + 25, g1[j][1] + 25), 5)
for i in g1:
    pygame.draw.rect(SCREEN, (50, 50, 200), (g1[i][0], g1[i][1], 50, 50), 0)

pygame.display.flip()
#pygame.time.delay(5000)
SCREEN.blit(FONT.render('INPUT NETWORK',True,(255,0,0)),(200,25))
SCREEN.blit(FONT.render('b1', True, (255,0,0)), (75,75))
SCREEN.blit(FONT.render('b2', True, (255,0,0)), (525,75))
SCREEN.blit(FONT.render('b3', True, (255,0,0)), (300,300))
SCREEN.blit(FONT.render('b4', True, (255,0,0)), (75,525))
SCREEN.blit(FONT.render('b5', True, (255,0,0)), (525,525))
SCREEN.blit(FONT.render('l1', True, (255,0,0)), (300,75))
SCREEN.blit(FONT.render('l2', True, (255,0,0)), (75,300))
SCREEN.blit(FONT.render('l3', True, (255,0,0)), (525,300))
SCREEN.blit(FONT.render('l4', True, (255,0,0)),(300,525))
pygame.display.update()
pygame.display.flip()
pygame.time.delay(5000)
l=[]
x={i:[] for i in g1}
for i in graph:
    if i!='b1':
        print(bfs(graph, 'b1',i))
        s=(bfs(graph, 'b1',i))
        l=s
        for i in range(len(l)-1):
            if l[i+1]  not in x[l[i]]:
                x[l[i]].append(l[i+1])
            if l[i] not in x[l[i+1]]:
                x[l[i+1]].append(l[i])

SCREEN.fill((0, 0, 0))

for i in x:
    if i.startswith('l'):
        continue
    for j in x[i]:
        pygame.draw.line(SCREEN, (255, 255, 255), (g1[i][0] + 25, g1[i][1] + 25), (g1[j][0] + 25, g1[j][1] + 25), 5)
for i in g1:
    pygame.draw.rect(SCREEN, (50, 50, 200), (g1[i][0], g1[i][1], 50, 50), 0)

pygame.display.flip()
#pygame.time.delay(10000)
SCREEN.blit(FONT.render('SPANNING TREE',True,(255,0,0)),(200,25))
SCREEN.blit(FONT.render('b1', True, (255,0,0)), (75,75))
SCREEN.blit(FONT.render('b2', True, (255,0,0)), (525,75))
SCREEN.blit(FONT.render('b3', True, (255,0,0)), (300,300))
SCREEN.blit(FONT.render('b4', True, (255,0,0)), (75,525))
SCREEN.blit(FONT.render('b5', True, (255,0,0)), (525,525))
SCREEN.blit(FONT.render('l1', True, (255,0,0)), (300,75))
SCREEN.blit(FONT.render('l2', True, (255,0,0)), (75,300))
SCREEN.blit(FONT.render('l3', True, (255,0,0)), (525,300))
SCREEN.blit(FONT.render('l4', True, (255,0,0)),(300,525))
pygame.display.update()
pygame.display.flip()
pygame.time.delay(10000)

pygame.quit()
