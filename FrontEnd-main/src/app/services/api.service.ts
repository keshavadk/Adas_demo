
import { HttpClient,HttpErrorResponse } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { Injectable, InjectionToken } from '@angular/core';
export const CONNECTION_TYPE = new InjectionToken<string>('ConnectionType');
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private _http:HttpClient) {
    
   }

  private user = new BehaviorSubject<any>(null);
   
  Currentuser = this.user.asObservable();
  Login_user(users: object) {
    this.user.next(users);
}
 
// login(Credential:any):Observable<any>{
//   return this._http.post("http://localhost:3000/login_api",Credential);
// }
// Gettask_list(): Observable<any>{
// return this._http.get("http://localhost:3000/Taskfile_list");
// }
Gettask_list(project_name): Observable<any>{
  return this._http.get(`http://localhost:8000/gettaskfilesfilteredonprojects/?project_name=${project_name}`);
  }
  
  login(user): Observable<any>{
    console.log(user);
    return this._http.post("http://127.0.0.1:8000/loginuser/", user);
    }
  GetObjectLevels(): Observable<any>{
      return this._http.get("http://localhost:8000/objectLevelAttributes");
  }
  GetSceneLevels(): Observable<any>{
    return this._http.get("http://localhost:8000/sceneLevelAtrributes");
  }

  GetprojectList(): Observable<any>{
    return this._http.get("http://localhost:8000/getProjectFilesname");
  }

  getmarking(project_name:any): Observable<any>{
    console.log(project_name);
    return this._http.get(`http://localhost:8000/getProjectFilesdetails/?project_name=${project_name}`);
  }

  post_withdatas(formdata){
    return this._http.post("http://localhost:8000/uploadAnnotationimages/", formdata);
  }

  Get_annotation_file(project_name:any,Filename:any){
    console.log(project_name,Filename);
    return this._http.get(`http://localhost:8000/getAnnotationImageFile/?project_name=${project_name}&File_Name=${Filename}`);
  }

}
