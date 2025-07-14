import cv2
import numpy as np

def extract_color_bounds(image_path, tolerance=20):
    # Load image with alpha channel (RGBA)
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    if image.shape[2] != 4:
        raise ValueError("Image does not have an alpha channel (expected RGBA).")

    # Split RGBA channels
    b, g, r, a = cv2.split(image)

    # Create mask of non-transparent pixels
    mask = a > 0

    # Stack RGB for processing
    rgb_pixels = np.dstack([r, g, b])[mask]

    # Compute RGB bounds
    lower_rgb = np.min(rgb_pixels, axis=0)
    upper_rgb = np.max(rgb_pixels, axis=0)

    # Add tolerance and clip
    lower_rgb = np.clip(lower_rgb - tolerance, 0, 255).astype(np.uint8)
    upper_rgb = np.clip(upper_rgb + tolerance, 0, 255).astype(np.uint8)

    # Include alpha for RGBA (assume fully opaque foreground)
    lower_rgba = np.append(lower_rgb, 255)
    upper_rgba = np.append(upper_rgb, 255)

    # Convert image to HSV and apply same mask
    rgb_image = cv2.merge([r, g, b])
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    hsv_pixels = hsv_image[mask]

    # Compute HSV bounds
    lower_hsv = np.min(hsv_pixels, axis=0)
    upper_hsv = np.max(hsv_pixels, axis=0)
    lower_hsv = np.clip(lower_hsv - tolerance, [0, 30, 30], [179, 255, 255]).astype(np.uint8)
    upper_hsv = np.clip(upper_hsv + tolerance, [0, 30, 30], [179, 255, 255]).astype(np.uint8)

    # Output results
    print("Lower RGBA:", lower_rgba.tolist())
    print("Upper RGBA:", upper_rgba.tolist())
    print("Lower RGB:", lower_rgb.tolist())
    print("Upper RGB:", upper_rgb.tolist())
    print("Lower HSV:", lower_hsv.tolist())
    print("Upper HSV:", upper_hsv.tolist())

    return lower_rgb, upper_rgb, lower_hsv, upper_hsv

# ==== Change this to your image path ====
image_path = "pingpong.png"

# Run
extract_color_bounds(image_path)
