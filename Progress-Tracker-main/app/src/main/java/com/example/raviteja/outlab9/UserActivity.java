package com.example.raviteja.outlab9;

import android.content.Context;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.ListView;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.Locale;

public class UserActivity extends AppCompatActivity {

    String username;
    TextView Name;
    TextView Company;
    TextView Location;
    ListView listView;
    ProgressBar progressBar;
    AsyncTaskRunner myAsyncTask;
    CustomAdapter customAdapter;
    static final String API_URL = "https://api.github.com/";
    ArrayList<String> names;
    ArrayList<String> ages;
    ArrayList<String> details;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user);
        Bundle user = getIntent().getExtras();
        username = user.getString("user");
        Name = (TextView) findViewById(R.id.text1);
        Company = (TextView) findViewById(R.id.text2);
        Location = (TextView) findViewById(R.id.text3);
        Name.setText(username);
        names = new ArrayList<String>();
        ages = new ArrayList<String>();
        details = new ArrayList<String>();
        listView = findViewById(R.id.listView);
        progressBar = (ProgressBar) findViewById(R.id.progressBar);
        customAdapter = new CustomAdapter(getApplicationContext(), names, ages, details);
        myAsyncTask = new AsyncTaskRunner();
        myAsyncTask.execute();
    }

    private class AsyncTaskRunner extends AsyncTask<Void, Void, List<String> > {

        @Override
        protected List<String> doInBackground(Void... urls) {

            try {
                URL url = new URL(API_URL + "users/" + username +  "/repos");
                URL url1 = new URL(API_URL + "users/" + username);
                HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                HttpURLConnection urlConnection1 = (HttpURLConnection) url1.openConnection();

                try {
                    BufferedReader bufferedReader1 = new BufferedReader(new InputStreamReader(urlConnection1.getInputStream()));
                    StringBuilder stringBuilder1 = new StringBuilder();
                    String line1;
                    while ((line1 = bufferedReader1.readLine()) != null) {
                        stringBuilder1.append(line1).append("\n");
                    }
                    bufferedReader1.close();
                    String result1 = stringBuilder1.toString();
                    JSONObject jo1 = new JSONObject(result1);
                    final String company = jo1.getString("company");
                    //Company.setText(company);
                    final String location = jo1.getString("location");
                    //Location.setText(location);
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            Company.setText(company);
                            Location.setText(location);
                        }
                    });

                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;
                    while ((line = bufferedReader.readLine()) != null) {
                        stringBuilder.append(line).append("\n");
                    }
                    bufferedReader.close();
                    String result = stringBuilder.toString();
                    try {
                        result = "{\"array\"=" + result + "}";
                        JSONObject jo = new JSONObject(result);
                        JSONArray jr = jo.getJSONArray("array");
                        for (int i = 0; i < jr.length(); i++) {
                            JSONObject st = jr.getJSONObject(i);
                            String repo_name = st.getString("name");
                            String repo_details = st.getString("description");
                            //String repo_age = st.getString("created_at");
                            String time_created = st.getString("created_at");//for ex: "2016-12-26T04:53:20Z"
                            String year = time_created.split("-")[0];
                            String month = time_created.split("-")[1];
                            String day = time_created.split("-")[2].substring(0,2);
                            int year_created = Integer.parseInt(year);
                            int month_created = Integer.parseInt(month);
                            int day_created = Integer.parseInt(day);
                            Calendar calendar = Calendar.getInstance();
                            //String current_date = DateFormat.getDateInstance().format(calendar.getTime());
                            String current_date = String.format(Locale.getDefault(), "%1$tm %1$td %1$tY", calendar);
                            int current_year = Integer.parseInt(current_date.split(" ")[2]);
                            int current_month = Integer.parseInt(current_date.split(" ")[0]);
                            int current_day = Integer.parseInt(current_date.split(" ")[1]);
                            int month_days[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
                            if (day_created > current_day) {
                                current_month = current_month - 1;
                                current_day = current_day + month_days[month_created - 1];
                            }
                            if (month_created > current_month) {
                                current_year = current_year - 1;
                                current_month = current_month + 12;
                            }
                            int calculated_day = current_day - day_created;
                            int calculated_month = current_month - month_created;
                            int calculated_year = current_year - year_created;
                            DecimalFormat formatter = new DecimalFormat("00");
                            String yy = formatter.format(calculated_year);
                            String mm = formatter.format(calculated_month);
                            String dd = formatter.format(calculated_day);
                            String repo_age = yy + " years " + mm + " months " + dd + " days";

                            names.add(repo_name);
                            Log.e("tag","added");
                            ages.add(repo_age);
                            details.add(repo_details);
                        }
                        Log.e("tag", "for loop executed");
                    } catch (JSONException e) {
                        e.printStackTrace();
                        Log.e("tag", "not working");
                    }
                    return names;
                } finally {
                    urlConnection.disconnect();
                }
            } catch (Exception e) {
                Log.e("ERROR", e.getMessage(), e);
                return null;
            }
        }


        protected void onPostExecute(List<String> response) {
            if (response == null) {
                Toast toast1 = Toast.makeText(getApplicationContext(),
                        "No Repositories",
                        Toast.LENGTH_SHORT);
                toast1.show();
            }
            progressBar.setVisibility(View.GONE);
            try {
                listView.setAdapter(customAdapter);
                Log.e("tag","adapter set");
                String s = Integer.toString(names.size()) + " repositories";
                Toast toast1 = Toast.makeText(getApplicationContext(),
                        s,
                        Toast.LENGTH_SHORT);

                toast1.show();
            } catch (Exception e) {
                Toast toast1 = Toast.makeText(getApplicationContext(),
                        "Error!!",
                        Toast.LENGTH_SHORT);
                toast1.show();
            }
        }

        @Override
        protected void onPreExecute() {
            progressBar.setVisibility(View.VISIBLE);
        }
    }

    public class CustomAdapter extends BaseAdapter {
        Context context;
        ArrayList<String> name;
        ArrayList<String> age;
        ArrayList<String> description;
        LayoutInflater inflter;

        public CustomAdapter(Context applicationContext, ArrayList<String> name, ArrayList<String> age , ArrayList<String> description) {
            this.context = applicationContext;
            this.name = name;
            this.age = age;
            this.description = description;
            inflter = (LayoutInflater.from(applicationContext));
        }

        @Override
        public int getCount() {
            return name.size();
        }

        @Override
        public Object getItem(int i) {
            return null;
        }

        @Override
        public long getItemId(int i) {
            return 0;
        }

        @Override
        public View getView(int i, View view, ViewGroup viewGroup) {
            view = inflter.inflate(R.layout.customs, null);
            TextView Name = (TextView) view.findViewById(R.id.text4);
            TextView Age = (TextView) view.findViewById(R.id.text5);
            TextView Description = (TextView) view.findViewById(R.id.text6);
            Name.setText(name.get(i));
            Age.setText(age.get(i));
            Description.setText(description.get(i));
            return view;
        }
    }
}




