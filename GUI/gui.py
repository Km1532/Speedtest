from tkinter import*
from PIL import Image, ImageTk
import speedtest
root = Tk()

root.geometry("1280x800")
root.title("Speed Test")
#image = Image.open("images.jpg")
#photo = ImageTk.PhotoImage(image)
def run_speedtest():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000
    ping = st.results.ping
    result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms")

test_button = Button(root, text="Run Speed Test", command=run_speedtest)
test_button.pack()

#canvas = Canvas(root, width=1280,height=800)

result_label = Label(root, text="")
result_label.pack()

#canvas.pack()
root.configure(background="black")
root.iconbitmap("icon.ico")
#canvas.create_image(0,0, anchor=NW, image=photo)

root.mainloop()




