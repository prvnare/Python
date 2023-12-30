import qrcode; 
# pip install Pillow 

class QRGenerator:
    def __init__(self, size:int, padding:int):
        self.qr =  qrcode.QRCode(box_size=size, border= padding);

    def create_qr(self, file_name:str, fg:str, bg:str):
        user_input = input('enter the text : ');
        try:
            self.qr.add_data(user_input);
            image = self.qr.make_image(fill_color=fg, back_color=bg);
            image.save(file_name);
            print(f'QR created. Saved at : {file_name}');
        except Exception as exception:
            print(f'exception : {exception}');


if __name__ == '__main__':
    QRGenerator(30,2).create_qr('sample.jpg', 'white','black');
