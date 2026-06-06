from kernels import SOBEL_HORIZONTAL
from processor import apply_convolution

if __name__ == "__main__":
    print("👁️  Initializing PixelKernel-CV Simulation Execution Layer...\n")

    # Creating a synthetic matrix simulating a high contrast white horizontal boundary edge
    mock_image = [
        [10,  10,  10,  10,  10],
        [10,  10,  10,  10,  10],
        [255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255]
    ]

    print("🖼️  Original Structural Grid Image Representation:")
    for row in mock_image:
        print(f"   {row}")

    processed_output = apply_convolution(mock_image, SOBEL_HORIZONTAL)

    print("\n⚡ Edge Feature Map Output Matrix (Post Horizontal Sobel Kernel):")
    for row in processed_output:
        print(f"   {row}")
