#!/usr/bin/env python3
import socket
import tkinter
import tkinter.messagebox
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_client():
    try:
        client.connect((ip_entry.get(), 7777))
        connected_label.config(text="Y", fg="green")
        tkinter.messagebox.showinfo("Connected", f"Connected to {ip_entry.get()}.")
    except ConnectionRefusedError as e:
        tkinter.messagebox.showinfo("Connection refused", e)

def send_message():
    message = message_tx.get()
    message_tx.delete(0, tkinter.END)
    
root = tkinter.Tk()
root.title("Socks (client)")
root.geometry("720x720")
root.configure(bg="gray")
ip_entry_label = tkinter.Label(root, text="Server IP", bg="gray", fg="#FFFFFF")
ip_entry_label.pack(anchor="n")
ip_entry = tkinter.Entry(root, insertbackground="gray", bg="#000000", fg="#FFFFFF")
ip_entry.pack(anchor="n")
connect_button = tkinter.Button(root, text="Connect!", bg="green", fg="black", command=connect_client)
connect_button.pack()
connected_label = tkinter.Label(root, text="N", bg="gray", fg="red")
connected_label.pack(anchor="n")
messages_rx = tkinter.Text(root, wrap="word", state="disabled", bg="#000000", fg="#FFFFFF", height=10, width=5)
messages_rx.pack(fill="both", anchor="n", pady=50)
message_tx = tkinter.Entry(root, bg="#000000", fg="#FFFFFF", width=50)
message_tx.pack()
message_tx_button = tkinter.Button(root, text="SEND", bg="blue", fg="#FFFFFF", command=send_message)
message_tx_button.pack(anchor="n")
root.mainloop()