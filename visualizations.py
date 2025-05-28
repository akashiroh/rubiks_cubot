import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_cube(cube_str: str):
    assert len(cube_str) == 54, "Cube string must be exactly 54 characters."

    # Color mapping
    letter_to_color = {
        'U': 'white',
        'D': 'yellow',
        'F': 'blue',
        'B': 'green',
        'L': 'red',
        'R': 'orange'
    }

    # Face order based on Singmaster layout
    face_order = ['U', 'R', 'F', 'D', 'L', 'B']

    # Map each face's facelet index to 3D cube coordinates
    face_positions = {
        'U': (lambda i: (i % 3, 2, i // 3), (0, 1, 0)),           # top face
        'D': (lambda i: (i % 3, 0, 2 - i // 3), (0, -1, 0)),      # bottom face (flip row)
        'F': (lambda i: (i % 3, 2 - i // 3, 2), (0, 0, 1)),       # front face
        'B': (lambda i: (2 - i % 3, 2 - i // 3, 0), (0, 0, -1)),  # back face
        'L': (lambda i: (0, 2 - i // 3, i % 3), (-1, 0, 0)),      # left face
        'R': (lambda i: (2, 2 - i // 3, 2 - i % 3), (1, 0, 0)),   # right face
    }

    facelet_map = []
    idx = 0
    for face in face_order:
        mapping_func, normal = face_positions[face]
        for i in range(9):
            pos = mapping_func(i)
            color_letter = cube_str[idx]
            color = letter_to_color.get(color_letter, 'gray')  # fallback for unknown letters
            facelet_map.append((pos, normal, color))
            idx += 1

    # Calculate the vertices of a facelet
    def get_face_vertices(center, normal):
        x, y, z = center
        d = 0.48  # half-width
        if normal[0] != 0:  # X-normal (left/right)
            return [[x + 0.5 * normal[0], y - d, z - d],
                    [x + 0.5 * normal[0], y + d, z - d],
                    [x + 0.5 * normal[0], y + d, z + d],
                    [x + 0.5 * normal[0], y - d, z + d]]
        elif normal[1] != 0:  # Y-normal (up/down)
            return [[x - d, y + 0.5 * normal[1], z - d],
                    [x + d, y + 0.5 * normal[1], z - d],
                    [x + d, y + 0.5 * normal[1], z + d],
                    [x - d, y + 0.5 * normal[1], z + d]]
        elif normal[2] != 0:  # Z-normal (front/back)
            return [[x - d, y - d, z + 0.5 * normal[2]],
                    [x + d, y - d, z + 0.5 * normal[2]],
                    [x + d, y + d, z + 0.5 * normal[2]],
                    [x - d, y + d, z + 0.5 * normal[2]]]

    # Plotting
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    for pos, normal, color in facelet_map:
        verts = get_face_vertices(pos, normal)
        poly = Poly3DCollection([verts], facecolors=color, edgecolor='black')
        ax.add_collection3d(poly)

    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_zlim(-0.5, 3.5)
    ax.set_box_aspect([1, 1, 1])

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.view_init(elev=30, azim=-45)  # Adjust for best perspective

    plt.tight_layout()
    # plt.show()
    return fig
