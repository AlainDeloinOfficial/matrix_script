Here is just a stupid script to get an h@cker script or intelectual one (and show your reading skills with the --pdf)

I suggest to create an .exe with PyInstaller and add the following code on your PowerShell profile for a convenient use :

'''
function Show-Matrix {
    param (
        [Parameter(Mandatory=$false)]
        [string]$FilePath
    )

    $command = "D:\Informatique_perso\matrix\matrix.exe --pdf"

    Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "$command" -WindowStyle Maximized

}

Set-Alias -Name pause -Value Show-Matrix
'''