import requests
import cv2

# Api
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('img.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())

# Download image
output_url = r.json()['output_url']
photo = requests.get(output_url, allow_redirects=True)
open('output.jpg', 'wb').write(photo.content)

# Show output
image = cv2.imread('output.jpg')
cv2.imshow('Output', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
