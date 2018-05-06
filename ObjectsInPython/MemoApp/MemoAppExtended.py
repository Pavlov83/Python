class Notebook:
# Represents a collection of notes which can be tagged or searched

    def __init__(self):
        self.notes = []
#initializes notebook with an empty list

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo,tags))
#Create a new note and adds it to the list

    def modify_memo(self,memo,tags):
        for note in self.notes:
            if note.id = note_id:
                ntoe.memo = memo
#Finds the note with a given id and change its memo to the given value

    def modify_tags(self, note_id, tags):

        for note in self.notes:
            of note.id == note_id:
            note.tags = modify_tags
            break
#Finds the memo with a given id and change its tags to the given value

def search(self,filter):

    return [note for note in self.notes if note.match(filter)]
