using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;
using TMPro;
using System.Collections;
using System.Collections.Generic;

public class TestAPI : MonoBehaviour
{
    private string apiUrl = "http://127.0.0.1:8000/users/";
    public TextMeshProUGUI userListText;

    private void Start()
    {
        StartRequest();
    }

    public void StartRequest()
    {
        StartCoroutine(GetUsers());
    }

    private IEnumerator GetUsers()
    {
        UnityWebRequest request = UnityWebRequest.Get(apiUrl);
        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.ConnectionError || request.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError($"Error: {request.error}");
        }
        else
        {
            string responseBody = request.downloadHandler.text;
            UserList userList = JsonUtility.FromJson<UserList>("{\"users\":" + responseBody + "}");
            DisplayUsers(userList.users);
        }
    }

    private void DisplayUsers(List<User> users)
    {
        userListText.text = "";
        foreach (User user in users)
        {
            userListText.text += $"ID: {user.UserID}\n";
            userListText.text += $"Login: {user.Login}\n";
            userListText.text += $"Date Created: {user.PasswordHash}\n\n";
        }
    }
}
