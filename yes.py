class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.current_node = None

    def insert(self):
        music_name = input("Enter Music Name:\n")
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

    def delete_element(self):
        if self.head is None:
            print("No Music is there to delete!\n")
            return
        music_name = input("Enter Music Name to delete:\n")
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
        if self.head is None:
            print("Playlist is Empty!\n")
            return
        show_ptr = self.head
        i = 1
        print("Displaying Playlist :\n")
        while True:
            print(f"Song {i} : {show_ptr.data}")
            i += 1
            show_ptr = show_ptr.next
            if show_ptr == self.head:
                break

    def next_node(self):
        if self.current_node is None:
            print("No songs in Playlist!\n")
        else:
            self.current_node = self.current_node.next
            print(f"Playing Next Song : {self.current_node.data}")

    def prev_node(self):
        if self.current_node is None:
            print("No songs in Playlist!\n")
        else:
            self.current_node = self.current_node.prev
            print(f"Playing Previous Song : {self.current_node.data}")

    def first_node(self):
        if self.head is None:
            print("Playlist is Empty!\n")
        else:
            print(f"Playing First Music : {self.head.data}")

    def last_node(self):
        if self.head is None:
            print("Playlist is Empty!\n")
        else:
            print(f"Playing Last Music : {self.head.prev.data}")

    def specific_data(self):
        if self.head is None:
            print("No music is there to be searched!\n")
            return
        music_name = input("Enter Music Name to search:\n")
        ptr = self.head
        while True:
            if ptr.data == music_name:
                print("Music Found!\n")
                print(f"Playing Music : {ptr.data}")
                return
            ptr = ptr.next
            if ptr == self.head:
                break
        print("There is no Music file with this name!\n")

def main():
    playlist = Playlist()
    while True:
        print("\n-----Song Playlist Application-----\n")
        print("1. Add Music")
        print("2. Remove Music")
        print("3. Show Playlist")
        print("4. Play next file")
        print("5. Play previous file")
        print("6. Play first file")
        print("7. Play Last file")
        print("8. Play specific file")
        print("9. Exit\n")
        choice = int(input())
        if choice == 1:
            playlist.insert()
        elif choice == 2:
            playlist.delete_element()
        elif choice == 3:
            playlist.show()
        elif choice == 4:
            playlist.next_node()
        elif choice == 5:
            playlist.prev_node()
        elif choice == 6:
            playlist.first_node()
        elif choice == 7:
            playlist.last_node()
        elif choice == 8:
            playlist.specific_data()
        elif choice == 9:
            break

if __name__ == "__main__":
    main()


