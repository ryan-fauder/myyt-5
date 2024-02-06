import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../../environments/environment.development';
import { Video, VideoForm } from '../../../interfaces/video';

@Injectable({
  providedIn: 'root'
})
export class VideoService {
  apiUrl: string = environment.apiUrl;

  constructor(private _http: HttpClient) { }

  getVideoList(): Observable<Video[]>{
    return this._http.get<Video[]>(`${this.apiUrl}/videos`);
  }
  
  deleteVideo(id: number): Observable<Video>{
    return this._http.delete<Video>(`${this.apiUrl}/video?id=${id}`);
  }
  
  uploadVideo(video: any): Observable<Video>{
    return this._http.post<Video>(`${this.apiUrl}/upload`, video);
  }
  
  getVideo(id: number): Observable<Video>{
    return this._http.get<Video>(`${this.apiUrl}/video?id=${id}`);
  }

  searchVideo(name: string): Observable<Video[]>{
    return this._http.get<Video[]>(`${this.apiUrl}/video?name=${name}`)
  }

  streamVideo(id: number): Observable<Video>{
    return this._http.get<Video>(`${this.apiUrl}/stream?id=${id}`);
  }
}
