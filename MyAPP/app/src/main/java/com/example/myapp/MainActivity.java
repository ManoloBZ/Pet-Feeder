package com.example.myapp;


import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    EditText e1;
    String x;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void Boton(View view) {
        Toast.makeText(this, "Se ha servido la comida", Toast.LENGTH_SHORT).show();
        System.out.println("Se ha presionado el boton");
        BackgroundTask b = new BackgroundTask();
        b.execute("1");
    }
    class BackgroundTask extends AsyncTask<String,Void,Void>
    {
        Socket s;
        DataOutputStream dos;
        String  ip,message;

        @Override
        protected Void doInBackground(String... params)
        {
            ip="179.14.251.47";
            message=params[0];

            try {
                s = new Socket(ip,8080);
                dos = new DataOutputStream(s.getOutputStream());
                System.out.println("Se ha enviado info");
                dos.writeUTF(message);
                dos.close();
            }catch (IOException e){
                e.printStackTrace();
            }


            return null;
        }
    }
}