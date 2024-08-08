import requests

def teams(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns a list of data about all NHL teams including their id, venue details, division, conference, and franchise information.
    """
    url = "https://statsapi.web.nhl.com/api/v1/teams"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def team_stats(teamId: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns current season stats and the current season rankings for a specific team.
    """
    url = f"https://statsapi.web.nhl.com/api/v1/teams/{teamId}/stats"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
