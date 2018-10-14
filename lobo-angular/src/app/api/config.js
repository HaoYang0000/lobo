
export default function RestConfig(RestangularProvider){
    RestangularProvider.setBaseUrl('http://0.0.0.0:8732/api/');
    RestangularProvider.setDefaultHeaders(
        {
            Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImV4cCI6MTUzOTQ4NTQzNSwiaWF0IjoxNTM5NDg0NTM1fQ.PvZO4MGenK0kFDO5EKmbSZLLe-YhS5b4iU-HBl3GIQs"
        }
    );
}
