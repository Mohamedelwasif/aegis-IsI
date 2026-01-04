const axios = require('axios');

async function restoreSystem() {
    try {
        // 1. Login
        console.log('Logging in...');
        const loginRes = await axios.post('http://localhost:3000/api/auth/login', {
            username: 'admin',
            password: 'admin'
        });
        const token = loginRes.data.token;
        console.log('Login successful. Token acquired.');

        // 2. Get Backups
        console.log('Fetching backups...');
        const statusRes = await axios.get('http://localhost:3000/api/backup/status', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        
        const backups = statusRes.data.backups;
        if (!backups || backups.length === 0) {
            console.log('No backups found.');
            return;
        }

        const latestBackup = backups[0]; // Assuming sorted or picking the first one
        console.log(`Found backup: ${latestBackup.id} (${latestBackup.note})`);

        // 3. Restore
        console.log(`Restoring backup ${latestBackup.id}...`);
        const restoreRes = await axios.post(`http://localhost:3000/api/backup/restore/${latestBackup.id}`, {}, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        console.log('Restore Result:', restoreRes.data);

    } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
    }
}

restoreSystem();
