package com.example.rorro.binaryimagerecognition;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.ibm.watson.developer_cloud.android.library.camera.CameraHelper;
import com.ibm.watson.developer_cloud.visual_recognition.v3.VisualRecognition;
import com.ibm.watson.developer_cloud.visual_recognition.v3.model.ClassifyImagesOptions;
import com.ibm.watson.developer_cloud.visual_recognition.v3.model.ImageClassification;
import com.ibm.watson.developer_cloud.visual_recognition.v3.model.VisualClassification;
import com.ibm.watson.developer_cloud.visual_recognition.v3.model.VisualClassifier;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    // Creates Watson's Visual Recognition Image
    private VisualRecognition vrClient;
    // Creates Watson's Camera Helper
    private CameraHelper helper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Creates main App layout
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize Watson's Visual Recognition client
        vrClient = new VisualRecognition(
                VisualRecognition.VERSION_DATE_2016_05_20,
                getString(R.string.api_key)
        );

        // Initialize Watson's Camera Helper
        helper = new CameraHelper(this);
    }

    // Event handler when user presses the "Take Picture" Button
    public void takePicture(View view)
    {
        // Takes picture
        helper.dispatchTakePictureIntent();
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        super.onActivityResult(requestCode, resultCode, data);

        // Obtains image taken from default Camera App
        if(requestCode == CameraHelper.REQUEST_IMAGE_CAPTURE)
        {
            // Obtains bitmap picture of picture taken
            final Bitmap photo = helper.getBitmap(resultCode);
            // Obtains directory of where the picture taken was stored
            final File photoFile = helper.getFile(resultCode);

            // Obtains the ID of the ImageView and changes it's value
            // to the picture taken
            ImageView preview = findViewById(R.id.preview);
            preview.setImageBitmap(photo);

            // Executes a synchronous network request to Watson with the purpose of
            // classifying the picture taken
            AsyncTask.execute(new Runnable()
            {
                @Override
                public void run()
                {
                    VisualClassification response = vrClient.classify(new ClassifyImagesOptions.Builder().images(photoFile).build()).execute();

                    // Gives Watson the first picture on the list
                    ImageClassification classification = response.getImages().get(0);

                    // Watson treats each picture passed as a separate class
                    VisualClassifier classifier = classification.getClassifiers().get(0);

                    // Displays the results of the Image Recognition based if the
                    // results obtained are greater tha 70% accuracy
                    final StringBuffer output = new StringBuffer();
                    for(VisualClassifier.VisualClass object: classifier.getClasses())
                    {
                        if(object.getScore() > 0.7f)
                        {
                            output.append("Result: ").append(object.getName()).append("\n");
                        }
                    }

                    runOnUiThread(new Runnable()
                    {
                        @Override
                        public void run()
                        {
                            TextView detectedObjects = findViewById(R.id.detected_objects);
                            detectedObjects.setText(output);
                        }
                    });
                }
            });

        }
    }
}

