from ultralytics import YOLO
import os
import shutil 

model = YOLO('yolo12n.pt') 


def detect_objects(image_path, output_folder):
    # Perform inference
    results = model(image_path)

    detection_results = []
    for r in results:
        output_image_name = os.path.basename(image_path).split('.')[0] + '_detected.jpg'
        output_image_path = os.path.join(output_folder, output_image_name)
        
        # Save the annotated image directly to the output_folder
        r.save(filename=output_image_path)

        # Process results for JSON output
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist() # Bounding box coordinates
            confidence = box.conf[0].item()       # Confidence score
            class_id = box.cls[0].item()          # Class ID
            class_name = model.names[int(class_id)] # Class name

            detection_results.append({
                'box_coordinates': [x1, y1, x2, y2],
                'confidence': confidence,
                'class_id': int(class_id),
                'class_name': class_name
            })
    
    return output_image_path, detection_results
