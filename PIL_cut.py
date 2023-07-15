from PIL import Image
import os

def split_image(image_path, output_directory, size):
    # 打开图像
    image = Image.open(image_path)
    
    # 获取图像尺寸
    width, height = image.size
    
    # 计算图像水平和垂直方向上的切割数量
    num_horizontal_splits = width // size
    num_vertical_splits = height // size
    
    # 创建输出目录
    os.makedirs(output_directory, exist_ok=True)
    
    # 分割图像
    for i in range(num_horizontal_splits):
        for j in range(num_vertical_splits):
            # 计算每个小图像的区域
            left = i * size
            upper = j * size
            right = (i + 1) * size
            lower = (j + 1) * size
            
            # 裁剪图像
            small_image = image.crop((left, upper, right, lower))
            
            # 保存小图像
            small_image.save(os.path.join(output_directory, f'{i}_{j}.png'))

# 输入目录的路径
image_path = r'D:\imag\train\imag\Sentinel_export20.tif'

# 输出目录的路径
output_directory = r'D:\imag\train\imag\output'
size = 128  # 每个小图像的大小（宽度和高度）

split_image(image_path, output_directory, size)
