function verify-path{

    param([Parameter(Mandatory, ValueFromPipeline)] [string] $path, [string]$HashFile= "Hash_file.txt")

    process{
        
        $ruta= Test-Path -Path $path

        if ($ruta -eq $true){
            Get-ChildItem $path | Get-FileHash | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File $HashFile -Encoding ascii -ErrorAction SilentlyContinue
            Write-Host "Archivo creado con éxito (:"
        }else{

            Write-Host "La ruta no existe"
        }
        
    }
}
$fold= Read-Host "Ingresa el path: "
$fold | verify-path