# MONDRIAN TILES --------------------------------------------------------------

# In this example, we wil try to replicate a famous artwork by Piet Mondrian. This
# is a fairly simple design yet it has a beautiful effect. To do this, we will
# subdivide a canvas into subtiles and those subtiles into further subtiles and so 
# on until we reach a certain depth. We will achieve this through a recursive
# algorithm.
# Check out my blog post:
#       https://asanka.hashnode.dev/05-mondrian-tiles-drawing-with-code
#       https://asanka-sovis.blogspot.com/2022/06/05-mondrian-tiles-drawing-with-code.html
# Coded by Asanka Akash Sovis

# -----------------------------------------------------------------------------

tiles = []; # List that hold all the tiles

# Splitting Constants
splits = [0.3, 0.5, 0.7]; # Ratios to split a tile
optimumDepth = 10; # Depth to which the recursive algorithm must go

# Drawing Constants
spacing = 1; # Spacing between tiles
minSize = 10 # Minimum tile size to consider

# Colour palette
palette = ['#f3f3f3', '#f50f0f', '#fae316', '#0d7fbe', '#000000'] # The colour palette
# used by Piet Mondrian
paletteProb = [0.8, 0.05, 0.05, 0.05, 0.05] # Probabilities of each colour

def setup():
    global tiles # Calling the global tile list
    size(800, 800) # Size of the campus
    frameRate(1) # Frame rate
    background(palette[len(palette) - 1]) # Draw background
    
    tiles = split(0, 0, width, height, 0) # Calling the splitting function
    #println(tiles) # Printing the tile list
    drawTiles(tiles) # Drawing the tiles
    myText() # Drawing the text
    
    #saveFrame("Output\\Mondrian-" + str(frameCount) + ".png"); # Saves the current frame. Comment if you don't need
    
def draw():
    global tiles # Calling the global tile list
    background(palette[len(palette) - 1]) # Draw background
    
    drawTiles(tiles) # Drawing the tiles
    myText() # Drawing the text
    
    #saveFrame("Output\\Mondrian-" + str(frameCount) + ".png"); # Saves the current frame. Comment if you don't need
    
def split(myX, myY, myWidth, myHeight, depth):
    # Function that splits the tiles
    if ((depth == optimumDepth) or (myWidth < minSize) or (myHeight < minSize)):
        # If we've reached the maximum depth of recursive algorithm or the height or width is
        # lower than the maximum set, we return the tile without splitting
        return (myX, myY, myWidth, myHeight)
    
    else:
        # Otherwise we split it
        tile1 = 0
        tile2 = 0
        
        # We randomly decide if we split horizontally or vertically
        if (random(0, 1) > 0.5):
            # Decide the split position by randomly choosing a splitting ratio from
            # the list. Then create a tuple with the parameters
            splitSize = myWidth * splits[int(random(0, len(splits)))]
            tile1 = (myX, myY, splitSize, myHeight)
            tile2 = (myX + splitSize, myY,  myWidth - splitSize, myHeight)
            
        else:
            # Decide the split position by randomly choosing a splitting ratio from
            # the list. Then create a tuple with the parameters
            splitSize = myHeight * splits[int(random(0, len(splits)))]
            tile1 = (myX, myY, myWidth, splitSize)
            tile2 = (myX, myY + splitSize,  myWidth, myHeight - splitSize)
        
        # Returns the list, but instead of returning the split tiles, we again call the
        # split function on two new tiles to see if they can be split further
        # NOTE: This is called a recursive algorithm as the algorithm is
        #          recurring within itself
        return [split(tile1[0], tile1[1], tile1[2], tile1[3], depth + 1), split(tile2[0], tile2[1], tile2[2], tile2[3], depth + 1)]
        
def drawTiles(tileList):
    # Function that draws the tiles
    noStroke(); # Disabling the strokes
    
    # For each tile, we draw them
    # Again we have a recursive algorithm as we call the same function within itself
    # to draw the subtiles within tiles
    for item in tileList:
        if (type(item) is list):
            drawTiles(item)
            
        else:
            # If the item is a tuple, we draw it. We also make sure not to
            # draw tiles too small
            if ((item[2] > (spacing * 2)) and (item[3] > (spacing * 2))):
                drawTile(item[0], item[1], item[2], item[3]);
                
def drawTile(myX, myY, myWidth, myHeight):
    # Setting a fill colour for the tile from a random colour and draw the
    # tile as a rectangle
    fill(palette[randomDist()])
    rect(myX + spacing, myY + spacing, myWidth - (spacing * 2), myHeight - (spacing * 2))
    
def myText():
    # Drawing some text
    fill(palette[3])
    myFont = createFont("Calibri", 16)
    textFont(myFont)
    textAlign(CENTER, CENTER)
    
    textSize(60)
    text("MONDRIAN TILES", width/2, 200)
    
    textSize(30);
    text("BY ASANKA SOVIS", width / 2, 250);
    
def randomDist():
    # Function to choose a random colour but with a probability
    # This uses cumulative distributions to achieve this
    pdf = [(0, paletteProb[0]), (1, paletteProb[1]), (2, paletteProb[2]), (3, paletteProb[3]), (4, paletteProb[4])]
    cdf = [(i, sum(p for j,p in pdf if j < i)) for i,_ in pdf]
    
    return max(i for r in [random(0, 1)] for i,c in cdf if c <= r)
