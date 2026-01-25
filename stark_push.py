import os

def push(note):
    # standard signature for all ship commits
    signed_note = f"{note} ;-)"
    os.system('git add .')
    os.system(f'git commit -m "{signed_note}"')
    print(f"pushed: {signed_note}")

if __name__ == "__main__":
    desc = input("summary: ")
    push(desc)
