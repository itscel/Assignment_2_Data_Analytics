import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

if not os.path.exists('images'):
    os.makedirs('images') 

bar_img = mpimg.imread('images/bar.png')
sankey_img = mpimg.imread('images/sankey.png')
network_img = mpimg.imread('images/network.png')

fig = plt.figure(figsize=(12, 10))

fig.subplots_adjust(wspace=0.2, hspace=0.2)

ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(bar_img)
ax1.set_title('Bar Chart')

ax2 = fig.add_subplot(2, 2, 3)
ax2.imshow(sankey_img)
ax2.set_title('Sankey Diagram')

ax3 = fig.add_subplot(2, 2, (2, 4))  
ax3.imshow(network_img)
ax3.set_title('Network Graph')

collated_image_path = 'images/collated_output.png'
plt.savefig(collated_image_path, dpi=300, bbox_inches='tight')

plt.show()
