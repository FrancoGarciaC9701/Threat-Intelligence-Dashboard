def parse_abuseipdb_response(response):
    if not response or "data" not in response:
        return "No data found."

    data = response["data"]
    parsed = {
        "IP Address": data.get("ipAddress"),
        "Abuse Confidence Score": data.get("abuseConfidenceScore"),
        "Country": data.get("countryCode"),
        "Domain": data.get("domain"),
        "Total Reports": data.get("totalReports"),
        "Usage Type": data.get("usageType"),
        "ISP": data.get("isp"),
        "Last Reported At": data.get("lastReportedAt")
    }

    return parsed

def parse_virustotal_response(response):
    if not response or "data" not in response:
        return "No data found."

    attributes = response["data"]["attributes"]
    parsed = {
        "IP Address": response["data"].get("id"),
        "Country": attributes.get("country"),
        "Last Analysis Stats": attributes.get("last_analysis_stats"),
        "ASN": attributes.get("asn"),
        "Network": attributes.get("network")
    }

    return parsed
