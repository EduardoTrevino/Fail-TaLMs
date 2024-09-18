import requests
from typing import Optional

def get_remote_jobs(count: Optional[int] = 50, geo: Optional[str] = None, industry: Optional[str] = None, tag: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the latest remote job listings with optional filters.
    
    Parameters:
        count (Optional[int]): Number of listings to return (default: 50).
        geo (Optional[str]): Filter by job region.
        industry (Optional[str]): Filter by job category.
        tag (Optional[str]): Search by job title and description.
    
    Returns:
        JSON response with jobs.
    """
    url = "https://jobicy.com/api/v2/remote-jobs"
    params = {
        'count': count,
        'geo': geo,
        'industry': industry,
        'tag': tag
    }

    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_rss_feed(job_categories: Optional[str] = None, job_types: Optional[str] = None, search_keywords: Optional[str] = None, search_region: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve job listings in RSS format with optional filters.
    
    Parameters:
        job_categories (Optional[str]): Filter by job category.
        job_types (Optional[str]): Filter by job type.
        search_keywords (Optional[str]): Search by job title and description.
        search_region (Optional[str]): Filter by job region.
    
    Returns:
        RSS feed data.
    """
    url = "https://jobicy.com/"
    params = {
        'feed': 'job_feed',
        'job_categories': job_categories,
        'job_types': job_types,
        'search_keywords': search_keywords,
        'search_region': search_region
    }

    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    return response.content

def get_new_jobs_xml(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve XML formatted data of the most recent remote jobs.

    Returns:
        XML data with job listings.
    """
    url = "https://jobicy.com/feed/newjobs"
    response = requests.get(url)
    return response.content