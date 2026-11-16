import numpy as np

class ColorTranslator:
    def __init__(self, color):
        self.color = np.array(color, dtype = float)

    def rgb_to_yuv(self):
        color = self.color
        yuv = np.array(color)
        yuv[:,:,0] = 0.299*color[:,:,0] + 0.587*color[:,:,1] + 0.114*color[:,:,2]
        yuv[:,:,1]  = -0.147*color[:,:,0] - 0.289*color[:,:,1] + 0.436*color[:,:,2]
        yuv[:,:,2] = 0.615*color[:,:,0] -0.515*color[:,:,1] -0.100*color[:,:,2]
        return yuv


    def yuv_to_rgb(self):
        color = self.color
        rgb = np.array(color)
        # poder el max no està bé
        rgb[:,:,0] = max(min(color[:,:,0]+1.402*(color[:,:,2]-128), 255), 0)
        rgb[:,:,1]  = max(min(color[:,:,0] - 0.344136*(color[:,:,1]-128) -0.714136*(color[:,:,2]-128), 255), 0)
        rgb[:,:,2] = max(min(color[:,:,0] + 1.772*(color[:,:,1]-128), 255), 0)
        return rgb

    def rgb_yub_rgb(self):
        color = self.color
        print(color)
        result1 = self.rgb_to_yuv()
        print("rgb to yuv: ", result1)
        color = result1
        print("color de la segona vegada ", color)
        result2 = self.yuv_to_rgb()
        print("yub to rgb ", result2)
        return result2

color = np.array([[[0, 255, 255]]])

translator = ColorTranslator(color)
translator.rgb_yub_rgb()