import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '30s', target: 10 }, // ramp-up to 10 users
        { duration: '1m', target: 10 },  // stay at 10 users
        { duration: '30s', target: 0 },  // ramp-down to 0 users
    ],
};

export default function () {
    const res = http.get('http://<LoadBalancer-IP>/');
    if (res.status !== 200) {
        console.error(`Received non-200 response: ${res.status}`);
    }
    sleep(1);
}
