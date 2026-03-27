# Trouver tous les PID écoutant sur le port 8000 via netstat
netstat -ano | findstr :8000 | ForEach-Object {
    $line = $_.Trim()
    if ($line -match '\s+(\d+)$') {
        $pid = $Matches[1]
        # Tuer le PID
        taskkill /PID $pid /F
    }
}

# Lancer uvicorn
uvicorn main:myapp --reload