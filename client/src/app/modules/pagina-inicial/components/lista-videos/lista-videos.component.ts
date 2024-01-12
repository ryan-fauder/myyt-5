import { Component, EventEmitter, Input, OnChanges, Output, SimpleChanges } from '@angular/core';
import { Video } from '../../../../interfaces/video';
import {MatListModule} from '@angular/material/list';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-lista-videos',
  standalone: true,
  imports: [
    MatListModule
  ],
  templateUrl: './lista-videos.component.html',
  styleUrl: './lista-videos.component.css'
})
export class ListaVideosComponent {
  @Input() videos: Video[] | null = [];
  @Output() selectVideo = new EventEmitter();


  playVideo(item: Event, id: number){
    this.selectVideo.emit(id);
  }
}
