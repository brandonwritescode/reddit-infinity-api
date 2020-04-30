const request = require('request')
const expect = require('chai').expect

describe('/GET /', () => {
    it('Should return status 200', (done) => {
        request('/', (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            done();
        });
    });
});