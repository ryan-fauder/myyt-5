import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Video } from '../../interfaces/video';
import { VideoService } from '../shared/services/video.service';
import { ListaVideosComponent } from './components/lista-videos/lista-videos.component';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-pagina-inicial',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    ListaVideosComponent,
    MatButtonModule,
    MatIconModule
  ],
  templateUrl: './pagina-inicial.component.html',
  styleUrl: './pagina-inicial.component.css'
})
export class PaginaInicialComponent {
  title = 'my-youtube-2';
  videos$!: Observable<Video[]>;
  videoToPlay: Video | null = null;
  videoUrl: string = ''
  constructor(private _videoService: VideoService){}
  ngDoCheck(): void {
    console.log('VideoToPlay: ', this.videoToPlay);
    
  }

  ngOnInit(): void {
    this.videos$ = this._videoService.getVideoList();
  }
  
  playVideo(id: number){
    this._videoService.getVideo(id).subscribe(
    video => {
      this.videoToPlay = video
      this.videoUrl = `http://localhost:5000/stream?id=${id}`
      console.log(this.videoToPlay);
    });
  }

  stream(id: number){
    this._videoService.streamVideo(id).subscribe(
    video => {
      this.videoToPlay = video
      console.log(this.videoToPlay);
    });
  }
}
