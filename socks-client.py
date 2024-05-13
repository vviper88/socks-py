#!/usr/bin/env python3
import socket
import tkinter
import tkinter.messagebox
import threading

connected = False
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def on_closing():
    client.close()
    root.destroy()

def connect_client():
    try:
        client.connect((ip_entry.get(), 7777))
        connected_label.config(text="Y", fg="green")
        tkinter.messagebox.showinfo("Connected", f"Connected to {ip_entry.get()}.")
        connected = True
    except ConnectionRefusedError as e:
        tkinter.messagebox.showinfo("Connection refused", e)

def rx_message():
    while True:
        msg_rx = client.recv(1024).decode("utf-8")
        messages_rx.insert(f"\n{msg_rx}")

def send_message():
    message = message_tx.get()
    
    if connected == True:
        message_tx.delete(0, tkinter.END)
        client.send(message.encode("utf-8"))
        if message == "!DC":
            client.close()
            connected = False
            connected_label.config(text="N", fg="red")
    else:
        tkinter.messagebox.showinfo("Error", "You are not connected to a server.")
        
root = tkinter.Tk()
root.title("Socks (client)")
root.geometry("480x480")
root.configure(bg="white")
ip_entry_label = tkinter.Label(root, text="Server IP", bg="white", fg="black")
ip_entry_label.pack(anchor="n")
ip_entry = tkinter.Entry(root, insertbackground="white", bg="#000000", fg="#FFFFFF")
ip_entry.pack(anchor="n")
connect_button = tkinter.Button(root, text="Connect!", bg="green", fg="black", command=connect_client)
connect_button.pack()
connected_label = tkinter.Label(root, text="N", bg="white", fg="red")
connected_label.pack(anchor="n")
messages_rx = tkinter.Text(root, wrap="word", state="disabled", bg="#000000", fg="#FFFFFF", height=10, width=50)
messages_rx.pack(anchor="n", pady=10)
message_tx = tkinter.Entry(root, insertbackground="grey", bg="#000000", fg="#FFFFFF", width=50)
message_tx.pack()
message_tx_button = tkinter.Button(root, text="SEND", bg="blue", fg="#FFFFFF", command=send_message)
message_tx_button.pack(anchor="n")
root.protocol("WM_DELETE_WINDOW", on_closing)

threading.Thread(target=rx_message)

root.mainloop()