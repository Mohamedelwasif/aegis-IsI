
$ErrorActionPreference = "Stop"

function Test-Behavioral-Analytics {
    Write-Host "--- Testing Behavioral Analytics ---" -ForegroundColor Cyan

    # 1. Login
    $loginUrl = "http://localhost:3000/api/auth/login"
    $loginBody = @{ username = "admin"; password = "admin" } | ConvertTo-Json
    try {
        $loginResponse = Invoke-RestMethod -Uri $loginUrl -Method Post -Body $loginBody -ContentType "application/json"
        $token = $loginResponse.token
        Write-Host "[+] Login Successful" -ForegroundColor Green
    } catch {
        Write-Error "Login Failed: $_"
    }

    # 2. Test Normal Behavior (Baseline: Login=9, Access=5, Data=10, Req=20)
    Write-Host "`n[Test 1] Normal Behavior Scenario..."
    $normalBody = @{
        userId = "test_user_001"
        metrics = @{
            loginTime = 9.5
            accessPattern = 6
            dataVolume = 12
            requestRate = 22
        }
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri "http://localhost:3000/api/v1/behavioral/analyze" -Method Post -Headers @{ Authorization = "Bearer $token" } -Body $normalBody -ContentType "application/json"
        if ($response.success -and $response.result.riskLevel -eq "normal") {
             Write-Host "[+] Normal Behavior Detected Correctly (Risk: $($response.result.riskLevel))" -ForegroundColor Green
        } else {
             Write-Host "[-] Failed Normal Test. Risk: $($response.result.riskLevel)" -ForegroundColor Red
        }
    } catch {
        Write-Error "Normal Test Failed: $_"
    }

    # 3. Test Critical Behavior (Massive Deviation)
    Write-Host "`n[Test 2] Critical Anomaly Scenario..."
    $criticalBody = @{
        userId = "test_user_001"
        metrics = @{
            loginTime = 3   # 3 AM (Avg 9) -> Dev ~3
            accessPattern = 50 # (Avg 5) -> Dev ~22.5
            dataVolume = 500   # (Avg 10) -> Dev ~98
            requestRate = 1000 # (Avg 20) -> Dev ~98
        }
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri "http://localhost:3000/api/v1/behavioral/analyze" -Method Post -Headers @{ Authorization = "Bearer $token" } -Body $criticalBody -ContentType "application/json"
        if ($response.success -and ($response.result.riskLevel -eq "critical" -or $response.result.riskLevel -eq "high")) {
             Write-Host "[+] Critical/High Risk Detected Correctly (Risk: $($response.result.riskLevel))" -ForegroundColor Green
             Write-Host "    Actions: $($response.result.actions -join ', ')"
        } else {
             Write-Host "[-] Failed Critical Test. Risk: $($response.result.riskLevel)" -ForegroundColor Red
        }
    } catch {
        Write-Error "Critical Test Failed: $_"
    }
}

Test-Behavioral-Analytics
