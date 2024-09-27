import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '30s', target: 50 }, // ramp-up to 50 users
        { duration: '1m', target: 50 },  // stay at 50 users
        { duration: '30s', target: 0 },  // ramp-down to 0 users
    ],
};

export default function () {
    const res = http.get('http://<your-service-ip>');
    if (res.status !== 200) {
        console.error(`Received non-200 response: ${res.status}`);
    }
    sleep(1);
}