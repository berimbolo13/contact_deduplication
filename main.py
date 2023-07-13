from contact_deduplication import get_contact_groups
from contact_model import Contact

if __name__ == '__main__':
    c1 = Contact(['ds@gmail.com'])
    c2 = Contact(['ds@apple.com'])
    c3 = Contact(['sw@apple.com'])
    c4 = Contact(['ds@gmail.com', 'ds@amazon.com'])
    c5 = Contact(['ds@apple.com', 'ds@gmail.com'])

    contacts = [c1, c2, c3, c4, c5]

    print(get_contact_groups(contacts=[c1, c2, c3, c4, c5]))
