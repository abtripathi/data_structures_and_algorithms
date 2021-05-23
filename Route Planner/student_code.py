import math

def shortest_path(M,start,goal):
    
    print("shortest path called")  
    
    ## calculate path length as euclidean distance
    def calculate_path_length(node_1,node_2):
        x,y = tuple(zip(M.intersections[node_1],M.intersections[node_2]))
        return math.sqrt(((x[0]-x[1])**2)+((y[0]-y[1])**2)) 
    
    ## heuristic is the euclidean distance between the node and the goal
    def calculate_heuristic(node):
        return calculate_path_length(node,goal)
     
     
    explored = set() ## set of explored nodes
    path_lengths = {start:0}  ## dict to store valid path lengths from start to any given node(key of dict)
    
    ## dict to store frontiers with key being the frontier node and the value as a tuple of total path cost to that
    ## node from start and the parent node through which this frontier is reached
    frontier= {start:(calculate_heuristic(start),start)} 
    
    ## shortest path which is the output of this algorithm
    shortest_path=list()   
    
    ## loop until all the frontiers are explored.break early if goaltest is successful
    while len(frontier) > 0:
        min_node = min(frontier,key=frontier.get) ## get the frontier node with minimum total cost path to explore         
        
        explored.add(min_node)
        
        ## goal test
        if min_node == goal:
            shortest_path.append(min_node)
            return shortest_path
        
        ## expanding new frontiers from the explored node   
        for children in M.roads[min_node]:            
            if children not in explored:   ## no need to expand, if already explored              
                g = path_lengths[min_node]+calculate_path_length(min_node,children) ## calculate path cost            
                h = calculate_heuristic(children)   ## calculate heuristic                
                f= g+h                              ## total path cost
                
                ## if expanded frontier not in the frontier dict.Add it
                ## update its path length in path_lengths dict
                ## any time a frontier is added, the corresponding parent node through which this frontier is reached is added
                ## into shortest path
                if children not in frontier:
                    frontier[children] = f,min_node
                    path_lengths[children] = g
                    if min_node not in shortest_path:
                        shortest_path.append(min_node)
                        
                ## if a frontier is already expanded, check if its existing total path cost is more than the new path cost to that
                ## frontier if new cost is less, remove the parent node from the shortest path through which that frontier was
                ## origianlly added. update the frontier with the new total cost and the new parent node 
              
                elif frontier[children][0] > f:                     
                    shortest_path.remove(frontier[children][1])                    
                    frontier[children] = f,min_node
                    path_lengths[children] = g    
                    
        ## delete the explored node from frontier dict    
        del frontier[min_node] 
        
    ## if we manage to reach at this point then that means path doesn't exist.return empty list    
    return []