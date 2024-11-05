package com.example.raviteja.outlab9;


import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;





public class SearchActivity extends AppCompatActivity {
    List<String> list_usernames;
    ArrayAdapter<String> adapter;
    EditText emailText;
    ProgressBar progressBar;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        emailText = (EditText) findViewById(R.id.emailText);
        progressBar = (ProgressBar) findViewById(R.id.progressBar);
        list_usernames = new ArrayList<String>();
        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, list_usernames);
        Button queryButton = (Button) findViewById(R.id.queryButton);
        queryButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new initial().execute();
            }
        });
    }

    class initial extends AsyncTask<Void, Void, List<String>> {

        private Exception exception;

        protected void onPreExecute() {
            list_usernames.clear();
            progressBar.setVisibility(View.VISIBLE);


        }

        protected List<String> doInBackground(Void... urls) {
            String email = emailText.getText().toString();
            // Do some validation here

            try {
                URL url = new URL("https://api.github.com/"+ "search/users?" + "q=" + email + "&" + "sort=repositories" + "&" + "order=desc");
                HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                try {
                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;
                    while ((line = bufferedReader.readLine()) != null) {
                        stringBuilder.append(line).append("\n");
                    }
                    bufferedReader.close();
                    String result = stringBuilder.toString();
                    try {
                        JSONObject jo = new JSONObject(result);
                        JSONArray jr = (JSONArray) jo.getJSONArray("items");
                        for (int i = 0; i < jr.length(); i++) {
                            JSONObject st = jr.getJSONObject(i);
                            String usern = st.getString("login");
                            list_usernames.add(usern);
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    return list_usernames;
                } finally {
                    urlConnection.disconnect();
                }
            } catch (Exception e) {
                Log.e("ERROR", e.getMessage(), e);
                return null;
            }
        }

        protected void onPostExecute(List<String> ans) {
            if (ans == null) {
                Toast toast_1 = Toast.makeText(getApplicationContext(),
                        "Error!!",
                        Toast.LENGTH_SHORT);
                toast_1.show();
            }
            progressBar.setVisibility(View.GONE);
            try {

                final ListView listView = findViewById(R.id.list_View);
                listView.setAdapter(adapter);

                Toast toast = Toast.makeText(getApplicationContext(),
                        "Search completed",
                        Toast.LENGTH_SHORT);
                toast.show();
                listView.setClickable(true);
                listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        //Object o= listView.getItemAtPosition(position);
                        String username =(String) listView.getItemAtPosition(position);

                        Intent intent = new Intent(SearchActivity.this, UserActivity.class);
                        intent.putExtra("username", username);
                        startActivity(intent);
                    }
                    //list_usernames=  new ArrayList<String>();
                });
            } catch (Exception toast) {
                Toast toast1 = Toast.makeText(getApplicationContext(),
                        "Error!!",
                        Toast.LENGTH_SHORT);
                toast1.show();
            }
        }
    }
}






































