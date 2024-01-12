import { Routes } from '@angular/router';
import { AdicionarVideoComponent } from './modules/adicionar-video/container/adicionar-video/adicionar-video.component';
import { PaginaInicialComponent } from './modules/pagina-inicial/pagina-inicial.component';

export const routes: Routes = [
    {
        path: '', pathMatch: 'full',
        component: PaginaInicialComponent
    },
    {
        path: 'upload', pathMatch: 'full',
        component: AdicionarVideoComponent
    }
];
