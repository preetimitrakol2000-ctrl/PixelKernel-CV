def apply_convolution(image_grid, kernel):
    img_height = len(image_grid)
    img_width = len(image_grid[0])
    k_size = len(kernel)
    pad = k_size // 2

    # Instantiating padded zero matrix coordinates
    padded_grid = [[0] * (img_width + 2 * pad) for _ in range(img_height + 2 * pad)]
    for r in range(img_height):
        for c in range(img_width):
            padded_grid[r + pad][c + pad] = image_grid[r][c]

    # Output grid instantiation
    output = [[0] * img_width for _ in range(img_height)]

    # Matrix Convolution Processing
    for r in range(img_height):
        for c in range(img_width):
            kernel_sum = 0.0
            for kr in range(k_size):
                for kc in range(k_size):
                    pixel = padded_grid[r + kr][c + kc]
                    weight = kernel[kr][kc]
                    kernel_sum += pixel * weight
            output[r][c] = max(0, min(255, int(kernel_sum))) # Clipping color range boundaries
            
    return output
