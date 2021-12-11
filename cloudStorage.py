import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9-S05DYcKoJFkmlECnTcz8v_6neo4HsU5CAoy-2PC4mgNir_8UGDZkpAJnrKEZ8IdVYdJaj43bkqh9MxM_OqINsDyJMuYBpG56a7XYvQMGdxTr9thF__lo-PPiXnkV_3l3kt_s'
    transferData = TransferData(access_token)
    
    file_from = input('enter the file patth to transfer:')
    file_to = input('path in dropbox:')

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()