import PySimpleGUI as sg

layout = [
    [sg.Text('Environment SetUp')],
    [sg.Text('Select Lab Environment', size=(20,1)), sg.Listbox([
        'AUK6b', 'AUK8a', 'AUK8b', 'AUK53a', 'AUK53b', 'AUK53c', 'AUK53d', 'AUK54a', 'AUK54b', 'AUK54c', 'AUK57a', 'AUK57b', 'AUK58a', 'AUK58b', 'AUK62a', 'AUK62b', 'AUK62c', 'AUK62d', 'AUK62e', 'AUK62f', 'AUK62g', 'AUK62h', 'AUK63a', 'AUK63b', 'AUK63c', 'AUK63d', 'AUK63e', 'AUK63f', 'AUK63g', 'AUK63h', 'AUK64a', 'AUK65a', 'AUK65b', 'BSR1b', 'DPA2a', 'DPA2b', 'DPA3', 'DYH1a', 'DYH1b', 'DYH2a', 'DYH2b', 'DYH3a', 'DYH3b', 'DYH4a', 'DYH4b', 'MDT15a', 'MDT17a', 'MDT17b', 'MDT18a', 'MDT18b', 'MDT19b', 'MDT20b', 'MDT21b', 'MDT22a', 'MTN08b', 'MTN17a', 'MTN23a', 'MTN23b', 'RDM5a', 'RDM5b', 'RDM6a', 'RDM6b', 'RDM52a', 'RDM52b', 'RDM52c', 'RDM52d', 'RDM52e', 'RDM52f', 'RDM53a', 'RDM53b', 'RDM53c', 'RDM53d', 'RDM54a', 'RDM54b', 'RDM54c', 'RDM55a', 'RDM55b', 'RDM55c', 'RDM55d', 'RDM55e', 'RDM55f', 'RDM56a', 'RDM56b', 'RDM56c', 'RDM56d', 'RDM56e', 'RDM57a', 'RDM59a', 'RDM59b', 'RDM59c', 'RDM60a', 'RDM60b', 'RDM60c', 'RDM60d', 'RDM60e', 'RDM60f', 'RDM60g', 'RDM61a', 'RDM61b', 'RDM61c', 'RDM61d', 'RDM61e', 'RDM61f', 'RDM61g', 'RDM62a', 'RDM62b', 'RDM62c', 'RDM62d', 'RDM62e', 'RDM62f', 'RDM63a', 'RDM64a', 'RDM64b', 'RDM65a', 'RDM65b', 'RDM66a', 'RDM66b', 'RDM66c', 'RDM66d', 'RDM67a', 'RDM67b', 'RDM68a', 'RDM68b', 'RDM68c', 'WNV1a',
        ], size=(8, 5))],
    [sg.Text('Enter your ATTUID:', size=(20,1)), sg.Input()],
    [sg.Text('Enter your Password:', size=(20,1)), sg.Input()],
    [sg.Button('Set Environment')],
    [sg.HorizontalSeparator()],
    [sg.Text('Environment Status Information')],
    [sg.Text(' 1. Lab Zone:', size=(20,1)), sg.StatusBar(' ')],
    [sg.Text(' 2. Tenant ID:', size=(20,1)), sg.StatusBar(' ')],
    [sg.Text(' 3. User ID:', size=(20,1)), sg.StatusBar(' ')],
    [sg.HorizontalSeparator()],
    [sg.Text('Provisioning Options')],
    [sg.Text(' 4. LDAP/Global Group Membership [Query/Add/Remove]', size=(50,1)), sg.Button('Select 4', size=(10,1))],
    [sg.Text(' 5. List Tenants', size=(50,1)), sg.Button('Select 5', size=(10,1))],
    [sg.Text(' 6. Query Provisioned User Roles', size=(50,1)), sg.Button('Select 6', size=(10,1))],
    [sg.Text(' 7. Add User Role to Tenant', size=(50,1)), sg.Button('Select 7', size=(10,1))],
    [sg.Text(' 8. Remove User Role from Tenant', size=(50,1)), sg.Button('Select 8', size=(10,1))],
    [sg.Text(' 9. Bulk Add Users to Tenant Role', size=(50,1)), sg.Button('Select 9', size=(10,1))],
    [sg.Text('10. Bulk Remove Users from Tenant Role', size=(50,1)), sg.Button('Select 10', size=(10,1))],
    [sg.Text('11. Show Sourced RC Environment Variables', size=(50,1)), sg.Button('Select 11', size=(10,1))],
    [sg.Text('12. Re-Enter Password [if mis-typed]', size=(50,1)), sg.Button('Select 12', size=(10,1))],
    [sg.Text('13. Reset Top Menu Choices 1, 2, 3', size=(50,1)), sg.Button('Select 13', size=(10,1))],
    [sg.Text('14. Instructions / About', size=(50,1)), sg.Button('Select 14', size=(10,1))],
    [sg.Text('15. Exit [ . ]', size=(50,1)), sg.Button('Select 15', size=(10,1))],
    [sg.HorizontalSeparator()],
    [sg.Text('Provisioning Sub-options')],
    [sg.Text('Sub-option 1', size=(20,1)), sg.Input()],
    [sg.Text('Sub-option 2', size=(20,1)), sg.Input()],
    [sg.Text('Sub-option 3', size=(20,1)), sg.Input()],
    [sg.Button('Submit')],
    [sg.HorizontalSeparator()],
    [sg.Text('Provisioning Results')],
    [sg.StatusBar('. . .', size=(60,10))],
]

window = sg.Window('Tenant UI', layout)

while True:
   event, values =  window.read()
   if event == sg.WIN_CLOSED:
       break
   
   elif event == 'Set Environment':
        print('Set Environment was pressed')

   elif event == 'Select 1':
        print('Select 1 was pressed')

   elif event == 'Select 2':
        print('Select 2 was pressed')

   elif event == 'Select 3':
        print('Select 3 was pressed')

   elif event == 'Select 4':
        print('Select 4 was pressed')

   elif event == 'Select 5':
        print('Select 5 was pressed')

   elif event == 'Select 6':
        print('Select 6 was pressed')

   elif event == 'Select 7':
        print('Select 7 was pressed')

   elif event == 'Select 8':
        print('Select 8 was pressed')

   elif event == 'Select 9':
        print('Select 9 was pressed')

   elif event == 'Select 10':
        print('Select 10 was pressed')

   elif event == 'Select 11':
        print('Select 11 was pressed')

   elif event == 'Select 12':
        print('Select 12 was pressed')

   elif event == 'Select 13':
        print('Select 13 was pressed')

   elif event == 'Select 14':
        print('Select 14 was pressed')

   elif event == 'Select 15':
        print('Select 15 was pressed')

window.close()
