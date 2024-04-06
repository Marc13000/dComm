#include <stdlib.h>
#include <curl/curl.h>
#include <iostream>
using namespace std;

void perform_request(){
    const char* API = getenv("API_KEY");
    if (API == NULL) {
        std::cerr << "API_KEY environment variable not set." << std::endl;
        return;
    }
    const string API_Header = "X-API-KEY: " + string(API);

    CURL *hnd = curl_easy_init();

    curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "GET");
    curl_easy_setopt(hnd, CURLOPT_WRITEDATA, stdout);
    curl_easy_setopt(hnd, CURLOPT_URL, "https://public-api.birdeye.so/public/tokenlist?sort_by=v24hUSD&sort_type=desc");

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, API_Header.c_str());
    curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

    CURLcode ret = curl_easy_perform(hnd);
    curl_easy_cleanup(hnd);
    if (headers != NULL) {
        curl_slist_free_all(headers);
    }

}

int main(){
    perform_request();
    return 0;
}