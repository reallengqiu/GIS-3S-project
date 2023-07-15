import os
from osgeo import gdal

def split_image(image_path, output_directory, size):
    # 打开归一化的图像
    dataset = gdal.Open(image_path)

    # 获取图像的宽度和高度
    width = dataset.RasterXSize
    height = dataset.RasterYSize

    # 计算水平和垂直方向上的切割数量
    num_horizontal_splits = width // size
    num_vertical_splits = height // size

    # 创建输出目录
    os.makedirs(output_directory, exist_ok=True)

    # 分割图像
    for i in range(num_vertical_splits):
        for j in range(num_horizontal_splits):
            # 计算每个小图像的区域
            top = i * size
            bottom = top + size
            left = j * size
            right = left + size

            # 创建输出文件路径
            output_file = os.path.join(output_directory, f'{i}_{j}.tif')

            # 裁剪图像
            gdal.Translate(output_file, dataset, format='GTiff', srcWin=[left, top, size, size])

    # 关闭数据集
    dataset = None


# 输入图像路径（归一化后的遥感图像）
image_path = r'D:\imag\train\imag\Sentinel_export20.tif'

# 输出目录的路径
output_directory = r'D:\imag\train\imag\output'

# 每个小图像的大小（宽度和高度）
size = 128

# 执行图像分割
split_image(image_path, output_directory, size)
