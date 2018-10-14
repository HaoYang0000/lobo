
export default function RestConfig(RestangularProvider){
    RestangularProvider.setBaseUrl('http://0.0.0.0:8732/api/');
    RestangularProvider.setDefaultHeaders(
        {
            Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImV4cCI6MTYyOTQ4NTUzOCwiaWF0IjoxNTM5NDg1NTM4fQ.SaGzEvKaJkxMlmcFMX4q7q1Xu-T70gwOqzg7X01Vh5g"
        }
    );
}
