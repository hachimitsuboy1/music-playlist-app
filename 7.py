import tkinter as tk
from tkinter import simpledialog

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.current_node = None

    def insert(self, music_name):
        new_node = Node(music_name)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = self.current_node = new_node
        else:
            last = self.head.prev
            new_node.prev = last
            last.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def delete_element(self, music_name):
        if self.head is None:
            print("No Music is there to delete!\n")
            return
        ptr = self.head
        while True:
            if ptr.next == ptr and ptr.data == music_name:
                print("One file deleted! Playlist is Empty Now!\n")
                self.head = None
                return
            elif ptr.data == music_name:
                prev = ptr.prev
                next = ptr.next
                prev.next = next
                next.prev = prev
                self.head = next
                print("Music deleted!\n")
                return
            ptr = ptr.next
            if ptr == self.head:
                break
        print("No Music file is there!\n")

    def show(self):
        playlist_contents = []
        if self.head is None:
            print("Playlist is Empty!\n")
        else:
            show_ptr = self.head
            i = 1
            while True:
                playlist_contents.append(f"Song {i}: {show_ptr.data}")
                i += 1
                show_ptr = show_ptr.next
                if show_ptr == self.head:
                    break
        return playlist_contents
def add_music(playlist, entry, listbox):
    music_name = entry.get()
    if music_name:
        playlist.insert(music_name)
        entry.delete(0, tk.END)
        refresh_playlist(playlist, listbox)

def delete_music(playlist, entry, listbox):
    music_name = entry.get()
    if music_name:
        playlist.delete_element(music_name)
        entry.delete(0, tk.END)
        refresh_playlist(playlist, listbox)

def refresh_playlist(playlist, listbox):
    listbox.delete(0, tk.END)
    playlist_contents = playlist.show()
    for item in playlist_contents:
        listbox.insert(tk.END, item)

def play_next(playlist):
    playlist.next_node()

def play_previous(playlist):
    playlist.prev_node()

def play_first(playlist):
    playlist.first_node()

def play_last(playlist):
    playlist.last_node()

def play_specific(playlist, entry):
    music_name = entry.get()
    if music_name:
        playlist.specific_data(music_name)
        entry.delete(0, tk.END)

def main():
    playlist = Playlist()

    root = tk.Tk()
    root.title("Song Playlist Application")

    entry_label = tk.Label(root, text="Music Name:")
    entry_label.grid(row=0, column=0, padx=5, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Add Music", command=lambda: add_music(playlist, entry, listbox))
    add_button.grid(row=0, column=2, padx=5, pady=5)

    delete_button = tk.Button(root, text="Delete Music", command=lambda: delete_music(playlist, entry, listbox))
    delete_button.grid(row=1, column=2, padx=5, pady=5)

    show_button = tk.Button(root, text="Refresh Playlist", command=lambda: refresh_playlist(playlist, listbox))
    show_button.grid(row=2, column=2, padx=5, pady=5)

    listbox = tk.Listbox(root)
    listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    next_button = tk.Button(root, text="Play Next", command=lambda: play_next(playlist))
    next_button.grid(row=4, column=0, padx=5, pady=5)

    previous_button = tk.Button(root, text="Play Previous", command=lambda: play_previous(playlist))
    previous_button.grid(row=4, column=1, padx=5, pady=5)

    first_button = tk.Button(root, text="Play First", command=lambda: play_first(playlist))
    first_button.grid(row=5, column=0, padx=5, pady=5)

    last_button = tk.Button(root, text="Play Last", command=lambda: play_last(playlist))
    last_button.grid(row=5, column=1, padx=5, pady=5)

    specific_button = tk.Button(root, text="Play Specific", command=lambda: play_specific(playlist, entry))
    specific_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()